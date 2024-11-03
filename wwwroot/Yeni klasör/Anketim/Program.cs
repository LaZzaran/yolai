using System.Diagnostics;
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

var app = builder.Build();

// Start FastAPI server
var startInfo = new ProcessStartInfo
{
    FileName = "python", // veya python3, iþletim sistemine göre
    Arguments = "career_counselor.py", // FastAPI script'inin yolu
    WorkingDirectory = "C:\\Users\\talha\\Desktop\\AnketApi\\Anket" // FastAPI script'inizin bulunduðu dizin
};

var fastApiProcess = Process.Start(startInfo);
app.Lifetime.ApplicationStopping.Register(() => fastApiProcess.Kill());

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();
app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
