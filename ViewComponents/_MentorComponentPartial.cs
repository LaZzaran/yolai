using BTK.DAL.Context;
using Microsoft.AspNetCore.Mvc;

namespace BTK.ViewComponents
{
    public class _MentorComponentPartial:ViewComponent
    {
        BtkContext context = new BtkContext();
        public IViewComponentResult Invoke()
        {
            var value = context.Mentors.ToList();
            return View(value);
        }
    }
}
