using BTK.DAL.Context;
using Microsoft.AspNetCore.Mvc;

namespace BTK.ViewComponents
{
    public class _AnketComponentPartial: ViewComponent
    {
        BtkContext context = new BtkContext();
        public IViewComponentResult Invoke()
        {
            var value = context.Ankets.ToList();
            return View(value);
        }
    }
}
