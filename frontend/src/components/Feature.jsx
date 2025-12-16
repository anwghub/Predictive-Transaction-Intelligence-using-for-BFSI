import React from 'react'
import chatbot from '../assets/chatbot.png';

const Feature = () => {
    return (
        <div className='relative overflow-hidden'>
            <section id="features" className="flex flex-col max-md:gap-20 md:flex-row pb-20 items-center justify-between mt-20 px-4 md:px-16 lg:px-24 xl:px-32">
                <img
                src={chatbot}
                alt="hero"
                className="max-w-xs sm:max-w-sm lg:max-w-md animate-float drop-shadow-[0_0_60px_rgba(180,120,255,0.35)]"
            />
                <div className="flex flex-col items-center md:items-start ml-10 ">

                    <ul className="text-lg text-center md:text-left text-current max-w-lg mt-4 font-bold">
                        Unlock smarter workflows with AI tools designed to boost productivity.
                    </ul>
                    <ul className="text-lg text-center md:text-left text-current max-w-lg mt-4 font-bold">
                        Chatbot for customer engagement
                    </ul>
                    <ul className="text-lg text-center md:text-left text-current max-w-lg mt-4 font-bold">
                        Chatbot for customer engagement
                    </ul>
                    <ul className="text-lg text-center md:text-left text-current max-w-lg mt-4 font-bold">
                        Unlock smarter workflows with AI tools designed to boost productivity.
                    </ul>

                </div>


            </section>
        </div>
    )
}

export default Feature