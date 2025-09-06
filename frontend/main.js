const { app, BrowserWindow, ipcMain } = require('electron')
const { spawn } = require('child_process')
const path = require('path')

let win
let pythonProccess = null

function startPython() {
    console.log("Запуск python")
    pythonProccess = spawn('python/python.exe', ['backend/main.py'])
    let buffer = ''; // Будем копить "недоделанные" JSON

    pythonProccess.stdout.on('data', (data) => {
    buffer += data.toString(); // Добавляем в буфер

    // Разбиваем по переводам строк
    const lines = buffer.split('\n');
    buffer = lines.pop(); // Последний может быть неполным — оставим в буфере

    lines.forEach(line => {
        if (line.trim() === '') return;

        try {
        const message = JSON.parse(line.trim());
        console.log('✅ Получено:', message);

        if (win) {
            win.webContents.send('python-data', message);
        }
        } catch (e) {
        console.error('❌ Ошибка парсинга JSON:', line);
        console.error('Буфер сейчас:', buffer);
        }
    });
});
}

function createWindow() {
    win = new BrowserWindow({
        width: 1000,
        height: 600,
        frame: false,
        resizable: true,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        }
    })
    const index_path = path.join(__dirname, '..', 'pyvoice-gui', 'dist', 'index.html')
    win.loadURL(`file://${index_path}`)

    startPython()
}

app.whenReady().then(() => {
    createWindow()

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow()
    })
})

ipcMain.on('python-cmd', (event, command) => {
  if (pythonProccess && command) {
    pythonProccess.stdin.write(command + '\n'); // Отправляем команду
  }
});

ipcMain.on('close-app', ()=> {
    if (win) win.close()
})

ipcMain.on('minimize', () => {
    if (win) win.minimize()
})

ipcMain.on('maximize', () => {
    if (win) {
        if (win.isMaximized()){
            win.restore()
        }
        else {win.maximize()}
    }
})


app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') app.quit()
})