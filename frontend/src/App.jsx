import { useState } from 'react';
import axios from "axios";
import { Input } from './components/ui/input';
import { Button } from './components/ui/button';
import { Card, CardContent } from './components/ui/card';
import { Sparkles } from 'lucide-react';
import { motion } from 'framer-motion';

function App() {
  const [keyword, setKeyword] = useState('');
  const [proverb, setProverb] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!keyword) return;
    setLoading (true);
    try {
      const respose = await axios.post('http://127.0.0.1:5000/generate', {keyword});
      setProverb(respose.data.proverb);
    } catch (error) {
      setProverb('Error generating your request, please try again later.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-yellow-100 via-white to-purple-100 flex flex-col items-center justify-center p-4">
      <motion.h1
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="text-4xl font-extrabold text-purple-700 flex items-center gap-2 mb-4"
      >
        <Sparkles className="w-8 h-8 text-yellow-500" /> Proverb Generator
      </motion.h1>

      <div className="w-full max-w-md bg-white rounded-2xl shadow-xl p-6 space-y-4">
        <Input
          placeholder="Enter a theme (e.g., courage, patience, wisdom)"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
          className="border-purple-300 focus:border-purple-500"
        />
        <Button
          onClick={handleGenerate}
          disabled={loading}
          className="w-full bg-purple-600 hover:bg-purple-700 text-white"
        >
          {loading ? 'Crafting wisdom...' : 'Generate Proverb'}
        </Button>

        {proverb && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.4 }}
          >
            <Card className="bg-yellow-50 border-2 border-purple-200 rounded-xl">
              <CardContent className="p-4 text-center">
                <p className="text-lg italic text-purple-700 whitespace-pre-line">{proverb}</p>
              </CardContent>
            </Card>
          </motion.div>
        )}
      </div>
    </div>
  );
}

export default App;