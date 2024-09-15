import Link from 'next/link'
import { PillLogo } from './logo'

export const Hero = () => {
  return (
    <div className="bg-gray-100 min-h-screen flex flex-col justify-center items-center px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl w-full space-y-8">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="space-y-6 text-center md:text-left">
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight text-gray-900">
              All Your Medication <br />All in One Place
            </h1>
            <p className="text-lg text-gray-700 max-w-xl mx-auto md:mx-0">
              At Pill Pal, our mission is to help people with busy lives keep their medication at the forefront of their mind. We know life gets hectic, and manually entering details into a reminder app can be a hassle. That's why we provide the ease of scanning your medication labels and creating automated reminders, so you never miss a dose.
            </p>
            <div className="flex justify-center md:justify-start">
              <Link
                href="/learn-more"
                className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
              >
                Learn More
              </Link>
            </div>
          </div>
          <PillLogo />
        </div>
    <br></br>
    <br></br>  
    <br></br>
    <br></br>  
    <br></br>
    <br></br>  
    <br></br>
    <br></br>  
    
        {/* Centered Privacy Policy Blurb */}
        <div className="text-center mt-8 text-sm text-gray-500 max-w-md mx-auto">
          <p>
            Your privacy is our priority. At Pill Pal, we take data security seriously and will never share your personal information with third parties. We are committed to keeping your medication details private and secure.
          </p>
        </div>
      </div>
    </div>
  )
}
