import React from 'react';
import { Outlet, Link, useNavigate } from 'react-router-dom';
import { useAuthStore } from '../../store/authStore';
import { LogOut, Home, Users, BookOpen, CheckSquare } from 'lucide-react';

export default function BaseLayout() {
  const { user, logout } = useAuthStore();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r border-gray-200">
        <div className="p-4 border-b border-gray-200">
          <h1 className="text-xl font-bold text-primary">AI2School</h1>
        </div>
        <nav className="p-4 space-y-2">
          <Link to="/" className="flex items-center space-x-2 p-2 rounded-md hover:bg-gray-100 text-gray-700">
            <Home className="w-5 h-5" />
            <span>Dashboard</span>
          </Link>
          <Link to="/staff" className="flex items-center space-x-2 p-2 rounded-md hover:bg-gray-100 text-gray-700">
            <Users className="w-5 h-5" />
            <span>Staff</span>
          </Link>
          <Link to="/students" className="flex items-center space-x-2 p-2 rounded-md hover:bg-gray-100 text-gray-700">
            <Users className="w-5 h-5" />
            <span>Students</span>
          </Link>
          <Link to="/courses" className="flex items-center space-x-2 p-2 rounded-md hover:bg-gray-100 text-gray-700">
            <BookOpen className="w-5 h-5" />
            <span>Courses</span>
          </Link>
          <Link to="/attendance" className="flex items-center space-x-2 p-2 rounded-md hover:bg-gray-100 text-gray-700">
            <CheckSquare className="w-5 h-5" />
            <span>Attendance</span>
          </Link>
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col">
        {/* Header */}
        <header className="bg-white border-b border-gray-200 h-16 flex items-center justify-between px-6">
          <h2 className="text-lg font-medium">Welcome</h2>
          <div className="flex items-center space-x-4">
            <span className="text-sm text-gray-600">{user?.email}</span>
            <button 
              onClick={handleLogout}
              className="flex items-center space-x-1 text-gray-500 hover:text-red-500 transition-colors"
            >
              <LogOut className="w-5 h-5" />
              <span className="text-sm">Logout</span>
            </button>
          </div>
        </header>

        {/* Page Content */}
        <div className="flex-1 p-6 overflow-auto">
          <Outlet />
        </div>
      </main>
    </div>
  );
}
