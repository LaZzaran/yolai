import { genAI } from "@/app/lib/gemini";
import { StreamingTextResponse } from 'ai';
import { ReadableStream } from 'stream/web';

// Allow streaming responses up to 30 seconds
export const maxDuration = 30;

export async function POST(req: Request) {
  const { messages } = await req.json();

  const model = genAI.getGenerativeModel({ model: "gemini-pro" });

  const prompt = messages.map((message: any) => message.content).join('\n');

  const result = await model.generateContentStream(prompt);

  const stream = new ReadableStream({
    async start(controller) {
      for await (const chunk of result.stream) {
        const text = chunk.text();
        controller.enqueue(text);
      }
      controller.close();
    },
  });

  // Cast the stream to unknown first, then to ReadableStream
  return new StreamingTextResponse(stream as unknown as ReadableStream);
}
