import React from 'react'
import { useNavigate } from 'react-router-dom'

const SideBar = () => {
  const navigate = useNavigate()

  const MenuItem = ({ icon: Icon, label, path }) => (
    <div
      onClick={() => navigate(path)}
      className="
        pb-10 text-xl flex items-center cursor-pointer
        justify-center md:justify-start
        gap-0 md:gap-2
      "
    >
      <Icon className="size-6 text-black" />
      <span className="hidden md:block text-black">{label}</span>
    </div>
  )

  return (
    <div
      className="
        w-16 md:w-1/5
        p-2
        pt-25
        h-screen
        bg-linear-to-r from-blue-500 to-purple-600
        sticky top-0
        overflow-y-auto
      "
    >
      <div className="font-bold text-xl space-y-10 p-4 mt-16">

        {/* Dashboard */}
        <MenuItem
          path="/dashboard"
          label="Dashboard"
          icon={(props) => (
            <svg {...props} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
              <path d="M18.375 2.25c-1.035 0-1.875.84-1.875 1.875v15.75c0 1.035.84 1.875 1.875 1.875h.75c1.035 0 1.875-.84 1.875-1.875V4.125c0-1.036-.84-1.875-1.875-1.875h-.75ZM9.75 8.625c0-1.036.84-1.875 1.875-1.875h.75c1.036 0 1.875.84 1.875 1.875v11.25c0 1.035-.84 1.875-1.875 1.875h-.75a1.875 1.875 0 0 1-1.875-1.875V8.625ZM3 13.125c0-1.036.84-1.875 1.875-1.875h.75c1.036 0 1.875.84 1.875 1.875v6.75c0 1.035-.84 1.875-1.875 1.875h-.75A1.875 1.875 0 0 1 3 19.875v-6.75Z" />
            </svg>
          )}
        />

        {/* Predict */}
        <MenuItem
          path="/predict"
          label="Prediction"
          icon={(props) => (
            <svg {...props} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
              <path d="M5.25 9a3 3 0 0 0-3 3v6a3 3 0 0 0 3 3h13.5a3 3 0 0 0 3-3v-6a3 3 0 0 0-3-3H15a.75.75 0 0 0-.75.75 2.25 2.25 0 0 1-4.5 0A.75.75 0 0 0 9 9H5.25Z" />
            </svg>
          )}
        />

        {/* Metrics */}
        <MenuItem
          path="/metrics"
          label="Metrics"
          icon={(props) => (
            <svg {...props} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
              <path fillRule="evenodd" d="M15.22 6.268a.75.75 0 0 1 .968-.431l5.942 2.28a.75.75 0 0 1 .431.97l-2.28 5.94a.75.75 0 1 1-1.4-.537l1.63-4.251-1.086.484a11.2 11.2 0 0 0-5.45 5.173.75.75 0 0 1-1.199.19L9 12.312l-6.22 6.22a.75.75 0 0 1-1.06-1.061l6.75-6.75a.75.75 0 0 1 1.06 0l3.606 3.606a12.695 12.695 0 0 1 5.68-4.974Z" />
            </svg>
          )}
        />

        {/* Alert */}
        <MenuItem
          path="/alert"
          label="Alert"
          icon={(props) => (
            <svg {...props} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
              <path fillRule="evenodd" d="M9.401 3.003c1.155-2 4.043-2 5.197 0l7.355 12.748c1.154 2-.29 4.5-2.599 4.5H4.645c-2.309 0-3.752-2.5-2.598-4.5L9.4 3.003ZM12 8.25a.75.75 0 0 1 .75.75v3.75a.75.75 0 0 1-1.5 0V9a.75.75 0 0 1 .75-.75Zm0 8.25a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Z" />
            </svg>
          )}
        />

        {/* History */}
        <MenuItem
          path="/history"
          label="History"
          icon={(props) => (
            <svg {...props} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
              <path fillRule="evenodd" d="M10.5 3A1.501 1.501 0 0 0 9 4.5h6A1.5 1.5 0 0 0 13.5 3h-3Zm-2.693.178A3 3 0 0 1 10.5 1.5h3a3 3 0 0 1 2.694 1.678c.497.042.992.092 1.486.15 1.497.173 2.57 1.46 2.57 2.929V19.5a3 3 0 0 1-3 3H6.75a3 3 0 0 1-3-3V6.257c0-1.47 1.073-2.756 2.57-2.93.493-.057.989-.107 1.487-.15Z" />
            </svg>
          )}
        />

      </div>
    </div>
  )
}

export default SideBar
