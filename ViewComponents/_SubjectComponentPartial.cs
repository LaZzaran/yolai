using BTK.DAL.Context;
using Microsoft.AspNetCore.Mvc;

namespace BTK.ViewComponents
{
    public class _SubjectComponentPartial : ViewComponent
    {
        BtkContext context = new BtkContext();
        public IViewComponentResult Invoke()
        {
            var value = context.Subjects.ToList();
            return View (value);
        }
    }
}
