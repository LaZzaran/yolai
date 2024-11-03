using BTK.DAL.Context;
using Microsoft.AspNetCore.Mvc;

namespace BTK.ViewComponents
{
    public class Presentation:ViewComponent
    {
        BtkContext context = new BtkContext();
        public IViewComponentResult Invoke()
        {
            var value = context.Presentations.ToList();
            return View(value);
        }
    }
}
