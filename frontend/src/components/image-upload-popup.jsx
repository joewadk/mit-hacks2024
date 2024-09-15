"use client"

import { useState } from "react"

import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Button } from "@/components/ui/button"
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription, DialogTrigger } from "@/components/ui/dialog"
import { Upload, Camera, ImagePlus } from "lucide-react";

export function ImageUploadPopup() {
  const [capturedImage, setCapturedImage] = useState(null)
  const [isOpen, setIsOpen] = useState(false)
  const [uploadedImages, setUploadedImages] = useState([]); 


  const handleFileUpload = (event) => {
    const files = event.target.files;
    if (files.length > 0) {
      const imageFiles = Array.from(files);
      const newImages = imageFiles.map((file) => {
        const reader = new FileReader();
        return new Promise((resolve) => {
          reader.onload = (e) => resolve(e.target?.result);
          reader.readAsDataURL(file);
        });
      });
      Promise.all(newImages).then((imageData) => setUploadedImages((prev) => [...prev, ...imageData]));
    }
  };
  

  const handleCapture = (event) => {
    const file = event.target.files?.[0]
    if (file) {
      const reader = new FileReader()
      reader.onload = (e) => setCapturedImage(e.target?.result)
      reader.readAsDataURL(file)
    }
  }

  const handleSubmit = () => {
    const request_url = 'http://127.0.0.1:5000/user-images';
    const request_param = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: uploadedImages}) 
    };

    fetch(request_url, request_param)
    .then(res => console.log(res.json()))
    .catch((err) => console.log(err))

    setIsOpen(false)
  }

  return (
    (<Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button className="flex items-center space-x-2">
          <ImagePlus className="w-4 h-4" />
          <span>Add Image or Details</span>
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px] md:max-w-[700px]">
        <DialogHeader>
          <DialogTitle>Image Upload or Manual Entry</DialogTitle>
          <DialogDescription>Choose how you want to provide the information</DialogDescription>
        </DialogHeader>
        <Tabs defaultValue="upload" className="w-full">
          <TabsList className="grid w-full grid-cols-3">
            <TabsTrigger value="upload">Upload Image</TabsTrigger>
            <TabsTrigger value="capture">Take Picture</TabsTrigger>
            <TabsTrigger value="manual">Manual Entry</TabsTrigger>
          </TabsList>
          <TabsContent value="upload">
            <div className="flex flex-col items-center space-y-4 pt-4">
              <Label htmlFor="image-upload" className="w-full">
                <div
                  className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer hover:bg-gray-50">
                  <Upload className="w-12 h-12 text-gray-400" />
                  <p className="mt-2 text-sm text-gray-500">Click to upload or drag and drop</p>
                </div>
                <Input
                  id="image-upload"
                  type="file"
                  accept="image/*"
                  className="hidden"
                  onChange={handleFileUpload} />
              </Label>
              {uploadedImages.length > 0 && (
              <div className="mt-4 grid grid-cols-3 gap-2">
                {uploadedImages.map((image, index) => (
                  <img
                    key={index}
                    src={image}
                    alt={`Uploaded ${index + 1}`}
                    className="max-w-full h-auto rounded-lg"
                    style={{ maxHeight: "200px" }} 
                    />
                    ))}
              </div>
            )}

            </div>
          </TabsContent>
          <TabsContent value="capture">
            <div className="flex flex-col items-center space-y-4 pt-4">
              <Label htmlFor="camera-capture" className="w-full">
                <div
                  className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer hover:bg-gray-50">
                  <Camera className="w-12 h-12 text-gray-400" />
                  <p className="mt-2 text-sm text-gray-500">Click to take a picture</p>
                </div>
                <Input
                  id="image-upload"
                  type="file"
                  accept="image/*"
                  multiple 
                  className="hidden"
                  onChange={handleFileUpload}
                />

              </Label>
              {capturedImage && (
                <div className="mt-4">
                  <img
                    src={capturedImage}
                    alt="Captured"
                    className="max-w-full h-auto rounded-lg" />
                </div>
              )}
            </div>
          </TabsContent>
          <TabsContent value="manual">
            <form className="space-y-4 pt-4">
              <div className="space-y-2">
                <Label htmlFor="name">Name</Label>
                <Input id="name" placeholder="Enter your name" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <Input id="email" type="email" placeholder="Enter your email" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="description">Description</Label>
                <Input id="description" placeholder="Enter a description" />
              </div>
            </form>
          </TabsContent>
        </Tabs>
        <div className="mt-6">
          <Button className="w-full" onClick={handleSubmit}>Submit</Button>
        </div>
      </DialogContent>
    </Dialog>)
  );
}