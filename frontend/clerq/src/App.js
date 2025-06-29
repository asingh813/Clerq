import { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [output, setOutput] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);
    const res = await axios.post("http://localhost:8001/upload/", formData);
    setOutput(res.data.analysis);
  };

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold mb-4">Clerq - AI Contract Assistant</h1>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleUpload} className="mt-4 bg-blue-500 text-white px-4 py-2">
        Analyze Contract
      </button>
      <pre className="mt-6 bg-gray-100 p-4 whitespace-pre-wrap">{output}</pre>
    </div>
  );
}

export default App;
