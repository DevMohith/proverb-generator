export function Card({ children, className = '' }) {
    return (
      <div className={`rounded-xl shadow-lg border p-4 bg-white ${className}`}>
        {children}
      </div>
    );
  }
  
  export function CardContent({ children, className = '' }) {
    return (
      <div className={`p-2 ${className}`}>
        {children}
      </div>
    );
  }
  