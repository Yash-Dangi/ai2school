import React from 'react';

export default function Dashboard() {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold text-gray-900">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h3 className="text-lg font-medium text-gray-900">Total Students</h3>
          <p className="text-3xl font-bold text-primary mt-2">1,234</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h3 className="text-lg font-medium text-gray-900">Active Courses</h3>
          <p className="text-3xl font-bold text-primary mt-2">42</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
          <h3 className="text-lg font-medium text-gray-900">AI Tokens Used</h3>
          <p className="text-3xl font-bold text-primary mt-2">15,400</p>
        </div>
      </div>
    </div>
  );
}
