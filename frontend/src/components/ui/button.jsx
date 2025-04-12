export function Button({ children, className = '', ...props }) {
    return (
      <button
        className={`px-4 py-2 rounded-lg font-semibold transition-all duration-200 disabled:opacity-50 ${className}`}
        {...props}
      >
        {children}
      </button>
    );
  }
  