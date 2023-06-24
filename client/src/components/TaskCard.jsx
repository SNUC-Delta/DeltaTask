import React from 'react'
import "../assets/css/TaskCard.css";

const TaskCard = ({task}) => {
  return (
    <div className="task-card">
      <h3>{task.title}</h3>
      <p>{task.description}</p>
      <p>Due Date: {task.dueDate}</p>
      <button id="edit">Edit</button>
      <button id="delete">Delete</button>
    </div>
  )
}

export default TaskCard