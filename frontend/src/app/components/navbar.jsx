"use client"

import { useState } from 'react'
import Link from 'next/link'
import { Menu, X } from 'lucide-react'

export const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <nav className="bg-[#962929] p-4">
      <div className="container mx-auto flex justify-between items-center">
        <div className="flex items-center">
        <svg
            className="w-10 h-10 transform -rotate-45"
            viewBox="0 0 100 100"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <rect
              x="10"
              y="30"
              width="80"
              height="40"
              rx="20"
              ry="20"
              fill="#EF4444"
            />
            <path
              d="M10 50C10 39.5066 18.5066 31 29 31H50V69H29C18.5066 69 10 60.4934 10 50Z"
              fill="#FCD34D"
            />
            <circle cx="75" cy="40" r="5" fill="white" />
          </svg>
          <span className="text-white text-xl font-bold">Pill Pal</span>
        </div>


        <div className="hidden md:flex space-x-4">
          <Link href="/" className="text-white hover:text-gray-200">
            Home
          </Link>
          <Link href="/pills" className="text-white hover:text-gray-200">
            Your Rx
          </Link>
          <Link href="/chat" className="text-white hover:text-gray-200">
            Chat
          </Link>
        </div>

        {/* Mobile menu button */}
        <div className="md:hidden">
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="text-white focus:outline-none"
          >
            {isOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </div>

      {/* Mobile menu */}
      {isOpen && (
        <div className="md:hidden">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
            <Link
              href="/"
              className="text-white block hover:bg-[#a33030] px-3 py-2 rounded-md"
            >
              Home
            </Link>
            <Link
              href="/pills"
              className="text-white block hover:bg-[#a33030] px-3 py-2 rounded-md"
            >
              Pills
            </Link>
            <Link
              href="/chat"
              className="text-white block hover:bg-[#a33030] px-3 py-2 rounded-md"
            >
              Chat
            </Link>
          </div>
        </div>
      )}
    </nav>
  )
}