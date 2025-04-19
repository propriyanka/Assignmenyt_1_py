import pipsutil
import time

def monitor_cpu_usage(threshold=80):
    """
    🚀 Step 1: Start monitoring CPU usage continuously.
    :param threshold: CPU usage percentage to trigger an alert (default: 80%)
    """
    print("🖥️ Monitoring CPU usage... Press Ctrl+C to stop.")
    
    try:
        while True:
            # 🔍 Step 2: Get the current CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"📊 Current CPU Usage: {cpu_usage}%")
            
            # ⚠️ Step 3: Check if CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"🚨 Alert! CPU usage exceeds threshold: {cpu_usage}% 🚨")
            
            # ⏳ Step 4: Wait for 1 second before checking again
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")
    except Exception as e:
        print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    # 🔧 Step 5: Set CPU threshold and start monitoring
    monitor_cpu_usage(threshold=80)
