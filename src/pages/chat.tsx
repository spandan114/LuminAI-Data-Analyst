import { useState } from 'react';
import { BiSend } from 'react-icons/bi';
import { BsStars } from 'react-icons/bs';
import Steps from '../components/Steps';
import SelectDataset from '../components/SelectDataset';
import BarChart from '../components/graphs/BarChart';

export default function Chat() {
  const [question, setQuestion] = useState('');
  const [processing, setProcessing] = useState(false);

  return (
    <div className="flex flex-col h-screen">
      <div className="my-8 mr-8  h-full rounded-[20px] bg-white border border-blue-gray-100 dark:bg-maroon-400 dark:border-maroon-600 flex justify-between w-full">
        <div className={`flex flex-col p-8 ${processing ? 'w-1/2' : 'w-full'}`}>
          {processing ? (
            <div className="bg-blue-gray-50 rounded-lg p-4">
              <div className="flex mb-4">
                <BsStars className="text-3xl text-navy-600 mb-2" />
                <p className="ml-2 text-navy-600">
                  The product category generating the most revenue is{' '}
                  <span className="text-green-600 font-bold">beleza_saude</span>
                </p>
              </div>

              <BarChart />
            </div>
          ) : (
            <SelectDataset />
          )}

          <div className="mt-auto flex justify-center items-center">
            {/* Centering container */}
            <div className={`relative ${processing ? 'w-full' : 'w-3/5'}`}>
              {/* Adjust max-width as needed */}
              <textarea
                className={`w-full h-40 p-4 bg-blue-gray-50 border-blue-gray-100 text-navy-600 placeholder-gray-400 border rounded-lg resize-none focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent`}
                placeholder="Type Your Question..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
              />
              <button
                onClick={() => {
                  setProcessing(true);
                }}
                className={`absolute bottom-4 right-4 border border-blue-gray-100 bg-white text-navy-800 p-2 rounded-lg transition-colors`}
              >
                <BiSend className="h-5 w-5" />
              </button>
              <button
                onClick={() => {
                  setProcessing(false);
                }}
                className={`absolute bottom-4 right-20 border border-blue-gray-100 bg-white text-navy-800 p-2 rounded-lg transition-colors`}
              >
                clear
              </button>
            </div>
          </div>
        </div>

        {processing && <Steps />}
      </div>
    </div>
  );
}
