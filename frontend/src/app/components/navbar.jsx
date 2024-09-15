export const Navbar = () => {
  return (
    <nav className="w-full bg-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          {/* Logo on the left */}
          <div className="flex-shrink-0 flex items-center">
            <a href="/" className="text-black font-bold text-2xl">Logo</a>
          </div>

          {/* Menu items on the right */}
          <div className="hidden md:flex items-center space-x-4">
            <a href="/" className="text-black hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium">Home</a>
            <a href="/" className="text-black hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium">About</a>
            <a href="/" className="text-black hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium">Services</a>
            <a href="/" className="text-black hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium">Contact</a>
          </div>
        </div>
      </div>
    </nav>
  );
}
