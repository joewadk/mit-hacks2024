import Link from 'next/link'
import { PillLogo } from './logo'

export const Hero = () => {
  return (
    <div className="bg-gray-100 min-h-screen flex items-center justify-center px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl w-full space-y-8">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="space-y-6 text-center md:text-left">
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight text-gray-900">
              All Your Pills In<br />One Place
            </h1>
            <div className="flex justify-center md:justify-start">
              <Link
                href="/learn-more"
                className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
              >
                Learn More
              </Link>
            </div>
          </div>
        <PillLogo/>
        </div>
        <p>*Data secured and not shared under any circumstances.</p>
      </div>
    </div>
  )
}