"use client";

import {
  Link,
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem,
} from "@nextui-org/react";
import { GithubIcon, HeyGenLogo } from "./Icons";
import { ThemeSwitch } from "./ThemeSwitch";

export default function NavBar() {
  return (
    <Navbar className="bg-gradient-to-r from-blue-900/70 via-indigo-900/70 to-purple-900/70 backdrop-blur-md border-b border-white/10">
      <NavbarBrand>
        <Link isExternal aria-label="HeyGen" href="https://app.heygen.com/">
          <HeyGenLogo />
        </Link>
        <div className="flex flex-col ml-2 md:ml-4">
          <p className="text-lg md:text-xl font-bold bg-gradient-to-br from-blue-300 to-purple-300 bg-clip-text text-transparent">
            Yapay Zeka İle Mülakat Hazırlığı
          </p>
          <p className="text-xs md:text-sm text-blue-200">
          İşe Alımda Devrim: Sizin Geleceğiniz, Bizim Zekamız          </p>
        </div>
      </NavbarBrand>
    </Navbar>
  );
}
