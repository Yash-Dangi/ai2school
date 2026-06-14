import React, { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '../lib/api';
import { CheckSquare, XSquare, Clock, MinusSquare } from 'lucide-react';

interface Student {
  id: string;
  admission_number: string;
  first_name: string;
  last_name: string;
}

interface AttendanceRecord {
  student_id: string;
  status: string;
}

export default function AttendancePage() {
  const queryClient = useQueryClient();
  const [date, setDate] = useState(new Date().toISOString().split('T')[0]);
  const [attendance, setAttendance] = useState<Record<string, string>>({});

  const { data: students, isLoading } = useQuery<Student[]>({
    queryKey: ['students'],
    queryFn: () => api.get('/student/'),
  });

  const saveAttendance = useMutation({
    mutationFn: (records: any) => api.post('/attendance/bulk', { records }),
    onSuccess: () => {
      alert("Attendance Saved Successfully");
    },
  });

  const handleStatusChange = (studentId: string, status: string) => {
    setAttendance(prev => ({
      ...prev,
      [studentId]: status
    }));
  };

  const handleMarkAll = (status: string) => {
    if (!students) return;
    const newAttendance: Record<string, string> = {};
    students.forEach(s => {
      newAttendance[s.id] = status;
    });
    setAttendance(newAttendance);
  };

  const handleSubmit = () => {
    const records = Object.entries(attendance).map(([student_id, status]) => ({
      student_id,
      date: new Date(date).toISOString(),
      status,
    }));
    if (records.length === 0) {
      alert("No attendance marked");
      return;
    }
    saveAttendance.mutate(records);
  };

  if (isLoading) return <div>Loading students...</div>;

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-semibold text-gray-900">Mark Attendance</h1>
        <div className="flex space-x-4 items-center">
          <input 
            type="date" 
            value={date}
            onChange={(e) => setDate(e.target.value)}
            className="rounded-md border-gray-300 shadow-sm focus:border-primary focus:ring-primary sm:text-sm border px-3 py-2"
          />
          <button
            onClick={handleSubmit}
            disabled={saveAttendance.isPending}
            className="bg-primary text-white px-4 py-2 rounded-md hover:bg-blue-600 transition-colors"
          >
            {saveAttendance.isPending ? 'Saving...' : 'Save Attendance'}
          </button>
        </div>
      </div>

      <div className="bg-white shadow-sm rounded-lg border border-gray-200 overflow-hidden p-4">
        <div className="flex justify-end space-x-2 mb-4">
          <button onClick={() => handleMarkAll('present')} className="text-xs bg-green-100 text-green-700 px-2 py-1 rounded">Mark All Present</button>
          <button onClick={() => handleMarkAll('absent')} className="text-xs bg-red-100 text-red-700 px-2 py-1 rounded">Mark All Absent</button>
        </div>

        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Student</th>
              <th className="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Present</th>
              <th className="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Absent</th>
              <th className="px-6 py-3 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Late</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {students?.map((student) => {
              const status = attendance[student.id];
              return (
                <tr key={student.id}>
                  <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                    {student.first_name} {student.last_name}
                    <span className="ml-2 text-xs text-gray-400">({student.admission_number})</span>
                  </td>
                  <td className="px-6 py-4 text-center">
                    <button 
                      onClick={() => handleStatusChange(student.id, 'present')}
                      className={`p-2 rounded-full ${status === 'present' ? 'bg-green-100 text-green-600' : 'text-gray-300 hover:bg-gray-100'}`}
                    >
                      <CheckSquare className="w-5 h-5" />
                    </button>
                  </td>
                  <td className="px-6 py-4 text-center">
                    <button 
                      onClick={() => handleStatusChange(student.id, 'absent')}
                      className={`p-2 rounded-full ${status === 'absent' ? 'bg-red-100 text-red-600' : 'text-gray-300 hover:bg-gray-100'}`}
                    >
                      <XSquare className="w-5 h-5" />
                    </button>
                  </td>
                  <td className="px-6 py-4 text-center">
                    <button 
                      onClick={() => handleStatusChange(student.id, 'late')}
                      className={`p-2 rounded-full ${status === 'late' ? 'bg-yellow-100 text-yellow-600' : 'text-gray-300 hover:bg-gray-100'}`}
                    >
                      <Clock className="w-5 h-5" />
                    </button>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
