using Microsoft.AspNetCore.Mvc;

namespace BTK.Controllers
{
    public class DefaultController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
        public IActionResult Sunum()
        {
            return ViewComponent("Presentation");
        } 
        public IActionResult Lesson()
        {
            return ViewComponent("_LessonComponentPartial");
        }  
        public IActionResult Subject()
        {
            return ViewComponent("_SubjectComponentPartial");
        }
        public IActionResult Team()
        {
            return ViewComponent("_TeamComponentPartial");
        }
        public IActionResult Mentor()
        {
            return ViewComponent("_MentorComponentPartial");
        }
        public IActionResult job()
        {
            return ViewComponent("_JobComponentPartial");
        }

    }
    }



