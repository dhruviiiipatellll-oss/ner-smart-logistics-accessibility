import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Dashboard() {
  const [stats, setStats] = useState({
    total_facilities: 156,
    total_patients: 2340,
    high_risk_patients: 342,
    accessibility_coverage: 67.5
  });

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Healthcare Facilities</h3>
          <p className="stat-value">{stats.total_facilities}</p>
          <p className="stat-label">Across NER Region</p>
        </div>
        <div className="stat-card">
          <h3>Elderly Patients</h3>
          <p className="stat-value">{stats.total_patients}</p>
          <p className="stat-label">Registered</p>
        </div>
        <div className="stat-card">
          <h3>High Risk Patients</h3>
          <p className="stat-value">{stats.high_risk_patients}</p>
          <p className="stat-label">Requiring Intervention</p>
        </div>
        <div className="stat-card">
          <h3>Accessibility Coverage</h3>
          <p className="stat-value">{stats.accessibility_coverage}%</p>
          <p className="stat-label">Population Covered</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;