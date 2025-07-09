import { appWindow } from '@tauri-apps/api/window'
import './App.css'

function App() {
  return (
    <div onMouseDown={() => appWindow.startDragging()}>
      <h1>Hello World</h1>
    </div>
  )
}

export default App
