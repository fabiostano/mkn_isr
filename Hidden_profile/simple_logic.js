const date = new Date();
const timestamp = date.getDate().toString().padStart(2, '0') + '-' +
                  date.getHours().toString().padStart(2, '0') + '-' +
                  date.getMinutes().toString().padStart(2, '0');
const DOMAIN = "193.196.39.63:443";
const roomName = "VideoMeeting-" + timestamp;
const FLASK_SERVER_URL = 'http://127.0.0.1:5000';
const RECORDING_DURATION = 0.25 * 60 * 1000; // Set to one minute

const options = {
    roomName: roomName,
    height: 700,
    parentNode: document.querySelector('#meet'),
    configOverwrite: {
        prejoinConfig: {
            enabled: false
        },
        startWithAudioMuted: false,
        startWithVideoMuted: false,
        TOOLBAR_BUTTONS: [
            'microphone', 'camera', 'desktop', 'fullscreen', 'fodeviceselection',
            'hangup', 'profile', 'chat', 'recording', 'livestreaming',
            'etherpad', 'sharedvideo', 'settings', 'raisehand',
            'videoquality', 'filmstrip', 'invite', 'feedback', 'stats',
            'shortcuts', 'tileview', 'download', 'help', 'mute-everyone'
        ]
    }
};

// Initialize Jitsi API
let api = new JitsiMeetExternalAPI(DOMAIN, options);

// Start interval recording
let recordingIndex = 0;
let recordingActive = true;  // Control the recording process

function startRecording() {
    api.executeCommand('startRecording', { mode: 'local', transcription: true });
}

function stopRecording() {
    api.executeCommand('stopRecording', 'local');
}

// Start the interval recording process
// Recording with delay
function intervalRecording() {
    const startNextRecording = () => {
        if (!recordingActive) return;

        console.log(`Recording ${recordingIndex} started.`);
        startRecording();
        setTimeout(() => {
            stopRecording();
            console.log(`Recording ${recordingIndex} stopped.`);
            recordingIndex++;
            setTimeout(startNextRecording, 2000); // 2-second delay
        }, RECORDING_DURATION);
    };
    startNextRecording();
}


// Fetch compound score from backend
function fetchCompoundScore() {
    console.log("fetching compound score of the current transcription");
    fetch(FLASK_SERVER_URL + '/get_vader_compound')
        .then(response => response.json())
        .then(data => {
            updateCompoundChart(data.compound)
        })
        .catch(error => {
            console.error('Error fetching compound value:', error);
        })
}

function fetchMeetingCompoundScore() {
    console.log("Fetching compound score of the meeting");
    fetch(FLASK_SERVER_URL + '/get_meeting_compound')
        .then(response => response.json())
        .then(data => {
            const compoundScore = data.compound;
            const scoreElement = document.getElementById('meeting-compound-score');

            // Display the meeting-wide compound score
            scoreElement.innerText = compoundScore;

            // Apply color based on score
            if (compoundScore > 0.2) {
                scoreElement.style.color = 'green';
            } else if (compoundScore < -0.2) {
                scoreElement.style.color = 'red';
            } else {
                scoreElement.style.color = 'orange';
            }

            // Prepare sentiment data for sending to the server
            const sentimentData = {
                timestamp: new Date().toISOString(),
                sentiment_compound: compoundScore
            };

            // Send data to the Flask backend
            fetch(FLASK_SERVER_URL + '/save_sentiment', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(sentimentData),
            })
                .then(response => response.json())
                .then(serverResponse => {
                    console.log('Sentiment data saved:', serverResponse);
                })
                .catch(error => {
                    console.error('Error saving sentiment data:', error);
                });
        })
        .catch(error => {
            console.error('Error fetching meeting compound value:', error);
        });
}




const ctx = document.getElementById('sentimentLineChart').getContext('2d');
const compoundChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],  // Labels will be updated dynamically
        datasets: [{
            label: 'VADER Compound Score',
            data: [],  // Data will be updated dynamically
            borderWidth: 2,
            fill: false,
            segment: {
                borderColor: (ctx) => {
                    const score = ctx.p0.parsed.y;  // Get the compound score of the starting point of each segment

                    if (score >= 0.05) return 'green';  // Positive sentiment
                    else if (score <= -0.05) return 'red';  // Negative sentiment
                    return 'orange';  // Neutral sentiment
                }
            },
            pointBackgroundColor: (ctx) => {
                const score = ctx.raw;  // Get the compound score for the point
                if (score >= 0.05) return 'green';
                else if (score <= -0.05) return 'red';
                return 'orange';
            }
        }]
    },
    options: {
        scales: {
            y: {
                min: -1,
                max: 1,
                title: { display: true, text: 'Compound Score' },
                ticks: {
                    stepSize: 0.1,
                    callback: function(value) {
                        if (value === 1) return 'Positive';
                        if (value === 0) return 'Neutral';
                        if (value === -1) return 'Negative';
                        return value.toFixed(1);
                    },
                    color: function(context) {
                        if (context.tick.value === 1) return 'green';
                        if (context.tick.value === 0) return 'orange';
                        if (context.tick.value === -1) return 'red';
                        return 'black';
                    }
                }
            },
            responsive: true,
            maintainAspectRatio: true,
            x: { title: { display: true, text: 'Transcriptions' } }
        },
        plugins: {
            annotation: {
                annotations: [
                    {
                        type: 'point',
                        xValue: 0,
                        yValue: 1,
                        backgroundColor: 'green',
                        radius: 5,
                        borderColor: 'green',
                        borderWidth: 1
                    },
                    {
                        type: 'point',
                        xValue: 0,
                        yValue: 0,
                        backgroundColor: 'orange',
                        radius: 5,
                        borderColor: 'orange',
                        borderWidth: 1
                    },
                    {
                        type: 'point',
                        xValue: 0,
                        yValue: -1,
                        backgroundColor: 'red',
                        radius: 5,
                        borderColor: 'red',
                        borderWidth: 1
                    }
                ]
            }
        }
    }
});


// Function to update chart with new data and color
function updateCompoundChart(compoundScore) {
    const color = compoundScore > 0.2 ? 'green' : compoundScore < -0.2 ? 'red' : 'yellow';
    compoundChart.data.labels.push(compoundChart.data.labels.length + 1);  // Increment label count
    compoundChart.data.datasets[0].data.push(compoundScore);               // Add new score
    compoundChart.data.datasets[0].borderColor = color;                    // Update line color
    compoundChart.data.datasets[0].pointBackgroundColor = color;           // Update point color
    compoundChart.update();
}

// Ensure the meeting is joined before starting recording
api.addEventListener('videoConferenceJoined', () => {
    console.log('Video conference joined');
    intervalRecording();
    //setup_question_form();

    // Fetch the summary and transcription every 20 seconds
    setInterval(() => {
        //fetchSummary();
        //fetchTranscription();
        fetchCompoundScore();
        fetchMeetingCompoundScore();
    }, RECORDING_DURATION);
});

// Cleanup routine -------------------

api.addEventListener('videoConferenceLeft', () => {
    console.log('Meeting ended. Triggering cleanup...');
    endMeetingCleanup();
    console.log("Meeting ended. Chart image sent to server.");
    sendChartImageToServer(compoundChart);
});

// Trigger cleanup via Flask backend
function endMeetingCleanup() {
    fetch(FLASK_SERVER_URL + '/cleanup_recordings', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            console.log('Cleanup status:', data.message);
        })
        .catch(error => {
            console.error('Error during cleanup:', error);
        });
}


function sendChartImageToServer(chart) {
    const imageBase64 = chart.toBase64Image(); // Get chart as Base64 image
    const payload = {
        image: imageBase64,
        timestamp: new Date().toISOString() // Optional: Add timestamp metadata
    };

    fetch(FLASK_SERVER_URL + '/store_chart_image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => {
        if (response.ok) {
            console.log('Chart image successfully sent to the server.');
        } else {
            console.error('Failed to send chart image to the server.');
        }
    })
    .catch(error => {
        console.error('Error sending chart image to the server:', error);
    });
}

