// Controllers/SubjectController.cs
using Microsoft.AspNetCore.Mvc;

public class SubjectController : Controller
{
    public IActionResult Index(string filter, string topic)
    {
        ViewBag.ActiveFilter = filter;
        ViewBag.Topic = topic;
        return View();
    }
}