



function startup() {
    connectButton = document.getElementById('connectButton');
    disconnectButton = document.getElementById('disconnectButton');
    sendButton = document.getElementById('sendButton');
    fileInputBox = document.getElementById('fileInput');
    downloadBox = document.getElementById('downloadBox');
    // to download from download box set:
    // downloadBox.src = "data:application/octet-stream;"

    // Set event listeners for buttons:
    connectButton.addEventListener('click', connectPeers, false);
    disconnectButton.addEventListener('click', disconnectPeers, false);
    sendButton.addEventListener('click', sendFile, false);
};

function connectPeers()
{
    localConnection = new RTCPeerConnection();

    sendChannel = localConnection.createDataChannel('sendChannel');
    sendChannel.onopen = handleSendChannelStatusChange;
    sendChannel.onclose = handleSendChannelStatusChange;

    //localConnection.addIceCandidate();
    
    // Following must be split up between this function and createRemoteConnection.
    localConnection.createOffer(/* set constraints */)
        .then(offer => localConnection.setLocalDescription(offer))
        .then(() => remoteConnection.setRemoteDescription(localConnection.localDescription))
        .then(() => remoteConnection.createAnswer())
        .then(answer => remoteConnection.setLocalDescription(answer))
        .then(() => localConnection.setRemoteDescription(remoteConnection.localDescription))
        .catch(handleCreateDescriptionError);
};

function createRemoteConnection()
{
    remoteConnection = new RTCPeerConnection();
    remoteConnection.ondatachannel = receiveChannelCallback;

    //localConnection.addIceCandidate();
};



// local's handler:
function handleSendChannelStatusChange(event)
{
    if (sendChannel) {
        var state = sendChannel.readyState;

        if (state == "open") {
            fileInputBox.disabled = false;
            fileInputBox.focus();
            sendButton.disabled = false;
            disconnectButton.disabled = false;
            connectButton.disabled = true;
        } else {
            fileInputBox.disabled = true;
            sendButton.disabled = true;
            disconnectButton.disabled = true;
            connectButton.disabled = false;
        }
    }
}
// remote's handler:
function handleSendChannelStatusChange(event)
{
    if (receiveChannel) {
        console.log("Receive channel's status has changed to " + receiveChannel.readyStatus);
    }
}

function sendFile()
{
    // Load file from file input, parse into blocks and block groups, and send them with verification procedure.
    console.log("FILE being SENT.");
}

function receiveChannelCallback(event)
{
    receiveChannel = event.channel;
    receiveChannel.onmessage = handleReceiveMessage;
    receiveChannel.onopen = handleReceiveChannelStatusChange;
    receiveChannel.onclose = handleReceiveChannelStatusChange;
}

function handleLocalAddCandidateSuccess()
{
    connectButton.disabled = true;
}

function handleRemoteAddCandidateSuccess()
{
    disconnectButton.disabled = false;
}

