import React, { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { api } from '../lib/api';
import { Sparkles, FileText } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

export default function LessonPlanner() {
  const [formData, setFormData] = useState({
    subject: '',
    grade_level: 10,
    topic: '',
    language: 'en'
  });

  const [lessonPlan, setLessonPlan] = useState('');

  const generatePlan = useMutation({
    mutationFn: (data: any) => api.post('/ai/lesson-plan', data),
    onSuccess: (response) => {
      setLessonPlan(response.lesson_plan);
    },
    onError: (err: any) => {
      alert("Error generating lesson plan: " + err.message);
    }
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setLessonPlan('');
    generatePlan.mutate(formData);
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-semibold text-gray-900">AI Curriculum Planner</h1>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-1 bg-white p-6 rounded-lg shadow-sm border border-gray-200 h-fit">
          <h3 className="text-lg font-medium mb-4 flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-primary" />
            Generate Plan
          </h3>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700">Subject</label>
              <input
                type="text"
                required
                value={formData.subject}
                onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
                placeholder="e.g. Science"
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary focus:ring-primary sm:text-sm border px-3 py-2"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Class/Grade Level</label>
              <input
                type="number"
                required
                min="1"
                max="12"
                value={formData.grade_level}
                onChange={(e) => setFormData({ ...formData, grade_level: parseInt(e.target.value) })}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary focus:ring-primary sm:text-sm border px-3 py-2"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Topic</label>
              <input
                type="text"
                required
                value={formData.topic}
                onChange={(e) => setFormData({ ...formData, topic: e.target.value })}
                placeholder="e.g. Laws of Motion"
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary focus:ring-primary sm:text-sm border px-3 py-2"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700">Output Language</label>
              <select
                value={formData.language}
                onChange={(e) => setFormData({ ...formData, language: e.target.value })}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary focus:ring-primary sm:text-sm border px-3 py-2"
              >
                <option value="en">English</option>
                <option value="hi">Hindi (हिन्दी)</option>
              </select>
            </div>
            <button
              type="submit"
              disabled={generatePlan.isPending}
              className="w-full flex justify-center items-center gap-2 py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary disabled:bg-blue-400 mt-4"
            >
              {generatePlan.isPending ? 'Generating with Gemini...' : 'Generate Curriculum'}
            </button>
          </form>
        </div>

        <div className="lg:col-span-2 bg-white p-6 rounded-lg shadow-sm border border-gray-200 min-h-[500px]">
          {generatePlan.isPending ? (
            <div className="flex flex-col items-center justify-center h-full text-gray-400 space-y-4">
              <Sparkles className="w-12 h-12 animate-pulse text-primary" />
              <p>AI is crafting your lesson plan...</p>
            </div>
          ) : lessonPlan ? (
            <div className="prose max-w-none">
              <ReactMarkdown>{lessonPlan}</ReactMarkdown>
            </div>
          ) : (
            <div className="flex flex-col items-center justify-center h-full text-gray-400 space-y-4">
              <FileText className="w-12 h-12" />
              <p>Your generated lesson plan will appear here.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
