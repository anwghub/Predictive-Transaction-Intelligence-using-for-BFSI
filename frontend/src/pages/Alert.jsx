import React from 'react'
import SideBar from '../components/SideBar'

const Alert = () => {
  return (
    <div className='flex min-h-screen'>
        <SideBar />
        
        <div className='bg-white md:mr-4 mt-25 md:ml-4 justify-center items-center flex-1 p-6 md:mt-25 mr-20 ml-25 mb-25  rounded-3xl'>
            <p className='text-black mt-5 text-2xl font-bold mb-6'>Show All Recent Alert Messages</p>
        </div>
    </div>
  )
}

export default Alert