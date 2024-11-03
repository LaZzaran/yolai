using BTK.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace BTK.Controllers
{
    public class AnketController : Controller
    {
        private readonly ILogger<AnketController> _logger;
        public AnketController(ILogger<AnketController> logger)
        {
            _logger = logger;
        }
        public IActionResult Index()
        {
            return View();
        }
        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
