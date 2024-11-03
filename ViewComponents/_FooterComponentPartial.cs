using BTK.DAL.Context;
using Microsoft.AspNetCore.Mvc;

namespace BTK.ViewComponents
{
    public class _FooterComponentPartial : ViewComponent
    {
  
        public IViewComponentResult Invoke()
        {
            return View();
        }
    }
}
