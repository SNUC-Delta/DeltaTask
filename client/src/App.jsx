import { useState } from "react";
import Navbar from "./components/Navbar";
import TaskCard from "./components/TaskCard";

function App() {
  const [count, setCount] = useState(0);
  const task = {
    title: 'Complete project',
    description: 'Finish building the todo list app',
    dueDate: '24-06-2023',
  };
  return (
    <>
      <main>
        <header>
          <Navbar />
          <TaskCard task={task}/>
        </header>
      </main>
    </>
  );
}

export default App;
