using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using System.Net.Http.Headers;

namespace BTK.Controllers
{
    public class ExamController : Controller
    {
        // PDF dosyasının sabit yolu
        private const string PdfFilePath = @"C:\Users\talha\Desktop\Ebob_Ekok_ve_aralarYnda_asal_sayYlar.pdf";

        // API URL’si
        private const string ApiUrl = "http://localhost:8000/upload-pdf/";

        public IActionResult Index()
        {
            return View();
        }
        public IActionResult Results()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> UploadPDF()
        {
            // FastAPI sunucusunu başlatma
            StartFastAPIServer();

            try
            {
                using (var client = new HttpClient())
                {
                    // PDF dosyasını byte dizisine çevirme
                    var fileBytes = System.IO.File.ReadAllBytes(PdfFilePath);
                    var content = new ByteArrayContent(fileBytes);
                    content.Headers.ContentType = new MediaTypeHeaderValue("application/pdf");

                    using (var formData = new MultipartFormDataContent())
                    {
                        formData.Add(content, "file", "Ebob_Ekok_ve_aralarYnda_asal_sayYlar.pdf");

                        var response = await client.PostAsync(ApiUrl, formData);
                        var responseString = await response.Content.ReadAsStringAsync();

                        if (response.IsSuccessStatusCode)
                        {
                            return Json(new { success = true, questions = responseString });
                        }
                        else
                        {
                            return Json(new { success = false, error = responseString });
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                return Json(new { success = false, error = $"Bir hata oluştu: {ex.Message}" });
            }
        }

        private void StartFastAPIServer()
        {
            var psi = new ProcessStartInfo
            {
                FileName = "python",
                Arguments = "-m uvicorn app:app --host 0.0.0.0 --port 8000",
                WorkingDirectory = @"C:\Users\talha\Desktop\BTK_Mini_Quiz\Api", // API dizininin yolu
                UseShellExecute = false,
                CreateNoWindow = true,
                RedirectStandardOutput = true,
                RedirectStandardError = true
            };

            Process.Start(psi);
        }
    }
}


