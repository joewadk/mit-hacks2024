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
            className="h-8 w-8 text-white mr-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M9 3h6m-6 16h6"
            />
          </svg>
          <span className="text-white text-xl font-bold">Logo</span>
        </div>

        {/* Desktop menu */}
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