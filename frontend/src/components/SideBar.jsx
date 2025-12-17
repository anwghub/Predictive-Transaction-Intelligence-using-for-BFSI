import React from 'react'
import { useNavigate } from 'react-router-dom'

const SideBar = () => {

  const navigate = useNavigate();

  return (
    <div className='w-1/5 p-2 py-30 min-h-screen bg-pink-200'>
      <div className='font-bold'>
        <div className='pb-10 text-xl mt-16 items-center'>
          <h2 className='text-black mb-4 items-center cursor-pointer' onClick={()=> navigate("/dashboard")}>Dashboard</h2>
        </div>
        <div className='pb-10 text-xl '>
          <h2 className='text-black mb-4 items-center cursor-pointer' onClick={()=> navigate("/predict")}>Predict Transaction</h2>
        </div>
        <div className='pb-10 text-xl '>
          <h2 className='text-black mb-4 items-center cursor-pointer' onClick={()=> navigate("/metrics")}>Transaction Metrics</h2>
        </div>
        <div className='pb-10 text-xl '>
          <h2 className='text-black mb-4 items-center cursor-pointer' onClick={()=> navigate("/alert")}>Alert</h2>
        </div>
        <div className='pb-10 text-xl '>
          <h2 className='text-black mb-4 items-center cursor-pointer' onClick={()=> navigate("/history")}>History</h2>
        </div>
      </div>


    </div>
  )
}

export default SideBar