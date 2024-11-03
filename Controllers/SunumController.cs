using BTK.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace BTK.Controllers
{
    public class SunumController : Controller
    {
        private readonly ILogger<SunumController> _logger;

        public SunumController(ILogger<SunumController> logger)
        {
            _logger = logger;
        }
        public IActionResult VideoPlayer()
        {
            return View();
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
   
