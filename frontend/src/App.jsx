import { useState } from 'react';
import axios from 'axios';
import { Input } from './components/ui/input';
import { Button } from './components/ui/button';
import { Card, CardContent } from './components/ui/card';
import { Sparkles, Copy } from 'lucide-react';
import { motion } from 'framer-motion';
import "./App.css";

function App() {
  const [keyword, setKeyword] = useState('');
  const [proverb, setProverb] = useState('');
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);

  const handleGenerate = async () => {
    if (!keyword) return;
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/generate', { keyword });
      setProverb(response.data.proverb);
      setCopied(false);
    } catch (err) {
      setProverb('⚠️ Error generating proverb. Please try again later.', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(proverb);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="app-wrapper">
      <div className="generated-card">
        <motion.h1
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <Sparkles style={{ marginRight: '10px', color: '#facc15' }} />
          Proverb Generator
        </motion.h1>

        <div>
          <Input
            type="text"
            placeholder="💡 Enter a theme (e.g., courage, patience, wisdom)"
            value={keyword}
            onChange={(e) => setKeyword(e.target.value)}
            className="input"
            style={{ height: '40px', width: '400px'}}
            onKeyDown={(e)=>{
              if (e.key === 'Enter'){
                handleGenerate();
              }
            }}
          />

          <Button
            onClick={handleGenerate}
            disabled={loading}
            className="button"
          >
            {loading ? '✨ Crafting Wisdom...' : '🔮 Generate Proverb'}
          </Button>

        </div>

        {proverb && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.4 }}
          >
            <div className="card" style={{ backgroundColor: '#fff', color: '#000', padding: '20px', borderRadius: '10px', position: 'relative' }}>
              <pre style={{ whiteSpace: 'pre-line', fontSize: '16px' }}>{proverb}</pre>
              <button onClick={handleCopy} style={{ position: 'absolute', top: '10px', right: '10px', background: 'none', border: 'none', cursor: 'pointer' }}>
                <Copy size={20} color="#6b21a8" />
              </button>
              {copied && <span style={{ position: 'absolute', top: '10px', right: '35px', fontSize: '12px', color: 'green' }}>Copied!</span>}
            </div>
          </motion.div>
        )}
      </div>
      <p className="footer-tag">💻 <a href='https://www.linkedin.com/in/mohithtummala/'>Mohith Tummala</a> — Website & GenAI Model Developer</p>
    </div>
  );
}

export default App;
