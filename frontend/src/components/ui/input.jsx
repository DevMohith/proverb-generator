export function Input({ className = '', ...props }) {
    return (
      <input
        className={`px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-400 transition-all duration-200 ${className}`}
        {...props}
      />
    );
  }
  