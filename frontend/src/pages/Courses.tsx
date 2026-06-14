import React, { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '../lib/api';
import { Plus, BookOpen } from 'lucide-react';

interface Subject {
  id: string;
  name: { [key: string]: string };
  code: string;
}

interface MasterSubject {
  code: string;
  name_en: string;
}

export default function Courses() {
  const queryClient = useQueryClient();
  const [isAdding, setIsAdding] = useState(false);
  const [selectedMasterCode, setSelectedMasterCode] = useState('');
  const [error, setError] = useState('');

  // Fetch subjects added by the school
  const { data: subjects, isLoading: isLoadingSubjects } = useQuery<Subject[]>({
    queryKey: ['subjects'],
    queryFn: () => api.get('/school/subjects'),
  });

  // Fetch master subject catalog
  const { data: masterSubjects, isLoading: isLoadingMaster } = useQuery<MasterSubject[]>({
    queryKey: ['masterSubjects'],
    queryFn: () => api.get('/school/master-subjects'),
  });

  // Create subject
  const createSubject = useMutation({
    mutationFn: (masterCode: string) => api.post('/school/subjects', { master_code: masterCode }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['subjects'] });
      setIsAdding(false);
      setSelectedMasterCode('');
      setError('');
    },
    onError: (err: any) => {
      setError(err.message || 'Failed to add course');
    }
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedMasterCode) {
      setError('Please select a course from the list');
      return;
    }
    setError('');
    createSubject.mutate(selectedMasterCode);
  };

  if (isLoadingSubjects || isLoadingMaster) return <div>Loading courses...</div>;

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-semibold text-gray-900">Manage Courses</h1>
        <button
          onClick={() => setIsAdding(!isAdding)}
          className="flex items-center space-x-2 bg-primary text-white px-4 py-2 rounded-md hover:bg-blue-600 transition-colors"
        >
          <Plus className="w-4 h-4" />
          <span>Add Course</span>
        </button>
      </div>

      {isAdding && (
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h3 className="text-lg font-medium mb-4">Add Course from Catalog</h3>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="max-w-md">
              <label className="block text-sm font-medium text-gray-700">Select Standard Course</label>
              <select
                required
                value={selectedMasterCode}
                onChange={(e) => setSelectedMasterCode(e.target.value)}
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-primary focus:ring-primary sm:text-sm border px-3 py-2"
              >
                <option value="" disabled>Select a course...</option>
                {masterSubjects?.map((ms) => (
                  <option key={ms.code} value={ms.code}>
                    {ms.name_en} ({ms.code})
                  </option>
                ))}
              </select>
            </div>
            
            {error && <p className="text-red-500 text-sm">{error}</p>}

            <div className="flex space-x-3">
              <button
                type="submit"
                disabled={createSubject.isPending}
                className="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary disabled:bg-blue-400"
              >
                {createSubject.isPending ? 'Saving...' : 'Add Course'}
              </button>
              <button
                type="button"
                onClick={() => {
                  setIsAdding(false);
                  setError('');
                }}
                className="px-4 py-2 border border-gray-300 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-50"
              >
                Cancel
              </button>
            </div>
          </form>
        </div>
      )}

      <div className="bg-white shadow-sm rounded-lg border border-gray-200 overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Code</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name (English)</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name (Hindi)</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {subjects?.length === 0 ? (
              <tr>
                <td colSpan={3} className="px-6 py-4 text-center text-sm text-gray-500">
                  <div className="flex flex-col items-center justify-center space-y-2">
                    <BookOpen className="w-8 h-8 text-gray-300" />
                    <p>No courses found. Add your first course to get started.</p>
                  </div>
                </td>
              </tr>
            ) : (
              subjects?.map((subject) => (
                <tr key={subject.id}>
                  <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{subject.code}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{subject.name.en}</td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{subject.name.hi || '-'}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
