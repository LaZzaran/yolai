using BTK.DAL.Context;
using Microsoft.AspNetCore.Mvc;

namespace BTK.ViewComponents
{
    public class _JobComponentPartial : ViewComponent
    {
        BtkContext context = new BtkContext();
        public IViewComponentResult Invoke()
        {
            var value = context.Jobs.ToList();
            return View(value);
        }
    }
}