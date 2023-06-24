import { useState } from "react";
import Navbar from "./components/Navbar";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <main>
        <header>
          <Navbar />
        </header>
      </main>
    </>
  );
}

export default App;
