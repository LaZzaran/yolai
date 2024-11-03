using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace BTK.Controllers
{
    public class QuastionController : Controller
    {
        public ActionResult AskQuestion()
        {
            return View();
        }

        // Python betiğini çalıştıran ve cevabı saklayan metod
        [HttpPost]
        public ActionResult RunPythonScript(string question)
        {

            // Python betiğinizin tam dosya yolunu buraya girin
            string pythonFilePath = @"C:\Users\talha\Desktop\searchAPI\findGEMINI.py";

            // Python betiğini çalıştır
            ProcessStartInfo start = new ProcessStartInfo
            {


                FileName = "python",
                Arguments = "findFEMINI.py",
                WorkingDirectory = pythonFilePath, // API dizininin yolu
                UseShellExecute = false,
                CreateNoWindow = true,
                RedirectStandardOutput = true,
                RedirectStandardError = true
            };

            try
            {
                using (Process process = Process.Start(start))
                {
                    // Python betiğinden dönen çıktıyı oku
                    string output = process.StandardOutput.ReadToEnd();
                    process.WaitForExit();

                    // Yanıtı ViewBag ile Answer sayfasına aktar
                    ViewBag.Answer = output;
                }
            }
            catch (Exception ex)
            {
                ViewBag.Answer = "Bir hata oluştu: " + ex.Message;
            }


            return RedirectToAction("Answer");
        }
        public ActionResult Answer()
        {
            return View();
        }
    }

}



