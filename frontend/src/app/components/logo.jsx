export const PillLogo = () => {
    return (
      <div className="w-32 h-32 md:w-48 md:h-48 lg:w-64 lg:h-64 relative">
        <div className="absolute inset-0 flex items-center justify-center">
          <svg
            className="w-full h-full transform -rotate-45"
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
        </div>
      </div>
    )
  }
  