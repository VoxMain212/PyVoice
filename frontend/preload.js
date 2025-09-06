const { contextBridge, ipcRenderer } = require('electron')


contextBridge.exposeInMainWorld('electronAPI', {
    sendCommand: (cmd) => ipcRenderer.send('python-cmd', cmd),
    onPythonData: (callback) => ipcRenderer.on('python-data', (event, data) => callback(data)),
    closeApp: () => ipcRenderer.send('close-app'),
    maximize: () => ipcRenderer.send('maximize'),
    minimize: () => ipcRenderer.send('minimize'),
    restore: () => ipcRenderer.send('restore-app')
})