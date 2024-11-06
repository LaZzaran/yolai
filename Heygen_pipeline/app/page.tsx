"use client";

import { AIChatBox } from "@/components/ai-chat-box";

export default function Home() {
  return (
    <main className="flex flex-col items-center min-h-screen bg-gradient-to-br from-blue-900 via-indigo-900 to-purple-900">
      <div className="w-full">
        <AIChatBox isVideoVisible={true} />
      </div>
    </main>
  );
}
