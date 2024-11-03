using BTK.DAL.Context;
using Microsoft.AspNetCore.Mvc;

namespace BTK.ViewComponents
{
    public class _LessonComponentPartial:ViewComponent
    {
        BtkContext context = new BtkContext();
        public  IViewComponentResult Invoke()
        {
            var values = context.Lessons.ToList();
            return View(values);
        }
    }
}
