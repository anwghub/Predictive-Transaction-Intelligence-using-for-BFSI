import React from 'react'
import SideBar from '../components/SideBar'

const Dashboard = () => {
  return (
    <div className="flex min-h-screen ">
      <SideBar />

      {/* Main Content */}
      <div className="flex-1 p-6 ml-20 mt-25 mr-15">
        
        {/* Header */}
        <h1 className="text-2xl font-bold mb-6">Dashboard</h1>

        {/* Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="bg-linear-to-r from-blue-500 to-purple-600 text-white p-6 rounded-xl hover:shadow-[0_0_20px_white]">
            <p className="text-sm text-blue-800 font-bold">Total Transactions</p>
            <h3 className="text-3xl font-bold mt-2">5000</h3>
          </div>

          <div className="bg-linear-to-r from-blue-500 to-purple-600 text-white p-6 rounded-xl hover:shadow-[0_0_20px_white]">
            <p className="text-sm text-blue-800 font-bold">Fraud Cases</p>
            <h3 className="text-3xl font-bold mt-2">120</h3>
          </div>

          <div className="bg-linear-to-r from-blue-500 to-purple-600 text-white p-6 rounded-xl hover:shadow-[0_0_20px_white]">
            <p className="text-sm text-blue-800 font-bold">Fraud Rate</p>
            <h3 className="text-3xl font-bold mt-2">2.4%</h3>
          </div>

          <div className="bg-linear-to-r from-blue-500 to-purple-600 text-white p-6 rounded-xl hover:shadow-[0_0_20px_white]">
            <p className="text-sm text-blue-800 font-bold">Top Active Customer</p>
            <h3 className="text-3xl font-bold mt-2">CUST-1021</h3>
          </div>
        </div>

        {/* Charts Section */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8 ">
          <div className="bg-white p-6 rounded-xl shadow h-300px text-black">
            {/* Chart 1 */}
            fraud vs Non-Fraud
          </div>
          <div className="bg-white p-6 rounded-xl shadow h-300px text-black">
            {/* Chart 2 */}
            Transaction by hour
          </div>
          <div className="bg-white p-6 rounded-xl shadow h-300px text-black">
            {/* Chart 1 */}
            Transaction by city
          </div>
          <div className="bg-white p-6 rounded-xl shadow h-300px text-black">
            {/* Chart 2 */}
            Transaction by channel
          </div>
        </div>

      </div>
    </div>
  )
}

export default Dashboard
