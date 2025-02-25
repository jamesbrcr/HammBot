import Link from 'next/link';

export default function Header() {
  return (
    <header className = "bg-black p-4 border-b-4 border-black">
      <nav className = "flex justify-between items-center max-w-4x1 mx-auto">
        <div className = "text-orange-200 font-bold">
          HammBot
        </div>
        <ul className = "flex space-x-4">
          {/* <li>
            <Link href="/" className = "text-orange-200 hover:text-orange-400">
                Hamm
            </Link>
          </li> */}
          <li>
            <Link href="/about" className="text-orange-200 hover:text-orange-400">
                About
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}
