import React from 'react'
import analytics from '../assets/analytics.png';

const Services = () => {
    return (
        <div className='relative overflow-hidden'>
            <section className="flex flex-col max-md:gap-20 md:flex-row pb-20 items-center justify-between mt-20 px-4 md:px-16 lg:px-24 xl:px-32">

                <div className="flex flex-col items-center md:items-start ">

                    <ul className="text-lg text-center md:text-left text-slate-200 max-w-lg mt-4 font-bold">
                        Unlock smarter workflows with AI tools designed to boost productivity.
                    </ul>
                    <ul className="text-lg text-center md:text-left text-slate-200 max-w-lg mt-4 font-bold">
                        Chatbot for customer engagement
                    </ul>
                    <ul className="text-lg text-center md:text-left text-slate-200 max-w-lg mt-4 font-bold">
                        Chatbot for customer engagement
                    </ul>
                    <ul className="text-lg text-center md:text-left text-slate-200 max-w-lg mt-4 font-bold">
                        Unlock smarter workflows with AI tools designed to boost productivity.
                    </ul>

                </div>
                <img
                    src={analytics}
                    alt="analytics"
                    className="max-w-xs sm:max-w-sm lg:max-w-md animate-float drop-shadow-[0_0_60px_rgba(180,120,255,0.35)]"
                />

            </section>
        </div>
    )
}

export default Services